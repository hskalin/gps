#!/usr/bin/env python
# coding: utf-8

import json
import ast
from tqdm import tqdm
from transformers import TrainingArguments
import torch
from transformers import BartForConditionalGeneration, BartTokenizerFast


def evaluate(logic_file, tokenizer_name, model_name, check_point, seq_num):

    # test_lst = range(2401, 3002)
        
    training_args = TrainingArguments("test_trainer")
    ## read logic form files
    with open(logic_file) as f:
        logic_forms = json.load(f)

    test_lst = range(len(logic_forms))
    print(len(test_lst))

    combined_logic_forms = {}
    for pid in test_lst:
        combined_logic_forms[pid] = logic_forms[str(pid)]['logic_forms']
                                    

    ## build tokenizer and model
    tokenizer = BartTokenizerFast.from_pretrained(tokenizer_name) # 'facebook/bart-base'
    model = BartForConditionalGeneration.from_pretrained(model_name).to(device) # 'facebook/bart-base'
    model.load_state_dict(torch.load(check_point))

    final = dict()
    for pid in tqdm(test_lst):
        input = str(combined_logic_forms[pid])
        tmp = tokenizer.encode(input)
        if len(tmp) > 10024:
            tmp = tmp[:10024]
        input = torch.LongTensor(tmp).unsqueeze(0).to(device)

        output = model.generate(input, bos_token_id=0, eos_token_id=2,
                             num_beams=10)
        print(output)
        print(len(output))

        ## refine output sequence
        seq = []
        for j in range(len(output)):
            res = tokenizer.decode(output[j].tolist())
            res = res.replace("</s>", "").replace("<s>", "").replace("<pad>", "")
            print(res)
            # try:
            #     res = ast.literal_eval(res) # string class to list class
            # except Exception as e:
            #     res = []
            seq.append(res)

        final[str(pid)] = {"id": str(pid), "num_seqs": seq_num, "seq": seq}

    return final


if __name__ == '__main__':

    logic_file = './data/logic_forms.json'
    constr_file = './data/constr_pred_correct.json'

    check_point = 'models/tp_model_4.pt'
    output_file = 'results/constr_pred.json'

    tokenizer_name = 'facebook/bart-base'
    model_name = 'facebook/bart-base'

    SEQ_NUM = 5

    device = torch.device('cpu')

    result = evaluate(logic_file, tokenizer_name, model_name, check_point, SEQ_NUM)

    with open(output_file, 'w') as f:
        json.dump(result, f)

