import torch
import torch.nn as nn
from Encoder import Encoder
from DecoderRNN import DecoderRNN


class seq2seq(nn.Module):
    def __init__(self, word_size_encoder, emb_dim, hidden_size, word_size_decoder, vector_size):
        super(seq2seq, self).__init__()
        self.encoder = Encoder(vector_size, word_size_encoder, emb_dim, hidden_size)
        self.decoder = DecoderRNN(hidden_size, word_size_decoder, vector_size)

    # input_encoder : vector of index
    def forward(self, input_encoder, input_decoder):
        output, hidden, hidden_list = self.encoder(input_encoder)
        output = self.decoder(input_decoder, hidden, hidden_list)
        return output
