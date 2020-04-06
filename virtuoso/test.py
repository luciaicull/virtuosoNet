import random
import os
import torch

from . import xml_utils

def load_file_and_generate_performance(args, test_path, composer, z, start_tempo, return_features=False):
    vel_pair = (int(args.velocity.split(',')[0]), int(
        args.velocity.split(',')[1]))
    test_x, xml_notes, xml_doc, edges, note_locations = xml_utils.read_xml_to_array(test_path, MEANS, STDS,
                                                                                    start_tempo, composer,
                                                                                    vel_pair)
    


def test(args,
         model,
         trill_model):
    # load checkpoint and check device
    if os.path.isfile('prime_' + args.modelCode + args.resume):
        print("=> loading checkpoint '{}'".format(args.modelCode + args.resume))
        filename = 'prime_' + args.modelCode + args.resume
        print('device is ', args.device)
        torch.cuda.set_device(args.device)
        if torch.cuda.is_available():
            def map_location(storage, loc): return storage.cuda()
        else:
            map_location = 'cpu'
        checkpoint = torch.load(filename, map_location=map_location)
        model.load_state_dict(checkpoint['state_dict'])
        print("=> loaded checkpoint '{}' (epoch {})"
              .format(filename, checkpoint['epoch']))

        trill_filename = args.trillCode + '_best.pth.tar'
        checkpoint = torch.load(trill_filename, map_location=map_location)
        trill_model.load_state_dict(checkpoint['state_dict'])
        print("=> loaded checkpoint '{}' (epoch {})"
              .format(trill_filename, checkpoint['epoch']))


    if args.sessMode == 'test':
        random.seed(0)
        load_file_and_generate_performance(
            args, args.testPath, args.composer, args.latent, args.startTempo)
