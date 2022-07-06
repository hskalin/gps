#!/usr/bin/env python
# coding: utf-8

import json
import torch
from torch.utils.data import Dataset
from random import choice

class GeometryDataset(Dataset):
    """Geometry dataset."""

    def __init__(self, logic_file, constr_file, tokenizer):

        self.tokenizer = tokenizer
        # self.split = split
        # assert self.split in ['train', 'val']

        # if self.split == 'train':
        #     self.pid_lst = range(0, 2101)
        # elif self.split == 'val':
        #     self.pid_lst = range(2101, 2401)
        #         
        with open(logic_file) as f:
            logic_forms = json.load(f)

        self.pid_lst = range(len(logic_forms))

        with open(constr_file) as f:
            constr_forms = json.load(f)

        self.combined_logic_forms = {}
        self.constr_forms = {}

        for pid in self.pid_lst:
            self.combined_logic_forms[pid] = logic_forms[str(pid)]['logic_forms']
            self.constr_forms[pid] = constr_forms[str(pid)]['constr_forms']

        
        # self.keys = sorted([int(i) for i in list(self.sequence.keys())])
        # print(len(self.keys))
        # print(max(self.keys))

        # self.valid_lst = [pid for pid in self.pid_lst if pid in self.keys ]
        # self.data = { i: self.combined_logic_forms[i] for i in self.pid_lst if i in self.keys }
        # self.sequences = { i: self.sequence[str(i)] for i in self.pid_lst if i in self.keys }


    def __len__(self):
        return len(self.pid_lst)

    def __getitem__(self, idx):

        # print(idx)
        pid = self.pid_lst[idx]

        ## input logic form sequence
        input = str(self.combined_logic_forms[pid])
        tokenized_inp = self.tokenizer.encode(input)
        if len(tokenized_inp) > 500:
            tokenized_inp = tokenized_inp[:500]

        torch.LongTensor(tokenized_inp)

        ## target theorem sequence
        # targets = self.sequences[pid]['seqs']
        # # target = choice(targets) # random choice one sequence
        # target = targets[0]  # min length

        # tokenized_tar = self.tokenizer.encode(str(target))
        # # print(tokenized_inp, tokenized_tar)

        output = str(self.constr_forms[pid])
        tokenized_tar = self.tokenizer.encode(output)
        if len(tokenized_tar) > 500:
            tokenized_tar = tokenized_tar[:500]

        torch.LongTensor(tokenized_tar)

        return tokenized_inp, tokenized_tar

