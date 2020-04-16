import os
import _pickle as cPickle

from pyScoreParser.musicxml_parser import MusicXMLDocument
from pyScoreParser import xml_utils

def read_xml_to_notes(path):
    xml_object = MusicXMLDocument(path)
    notes, rests = xml_object.get_notes()
    directions = xml_object.get_directions()
    time_signatures = xml_object.get_time_signatures()

    xml_notes = xml_utils.apply_directions_to_notes(
        notes, directions, time_signatures)
    
    return xml_object, xml_notes


def read_xml_to_array(xml_path, feature_path, feature_stats,
                      start_tempo, composer,
                      vel_pair):
    xml_object, xml_notes = read_xml_to_notes(xml_path)
    beats = xml_object.get_beat_positions()
    measure_positions = xml_object.get_measure_positions()
    
    with open(feature_path, "rb") as f:
        u = cPickle.Unpickler(f)
        feature_dict = u.load()
    
    test_x = feature_dict['input_data']
    note_locations = feature_dict['note_location']
    edges = feature_dict['graph']

    return test_x, xml_notes, xml_object, edges, note_locations
