import argparse
import json
from src.character import Character
from src.character_sheet_writer import CharacterSheetWriter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', metavar='config_json',
                        required=True,
                        help='specify character config JSON file')
    parser.add_argument('-i', '--infile', metavar='infile_pdf', 
                        default='character-sheet.pdf',
                        help='specify input PDF file')
    parser.add_argument('-o', '--outfile', metavar='outfile_pdf',
                        required=True,
                        help='specify output PDF file')
    args = parser.parse_args()

    with open(args.config) as file:
        data = json.load(file)

    character = Character(data["level"],
                          data["hit dice"],
                          data["abilities"],
                          data["proficiencies"],
                          data.get("spellbase"))

    writer = CharacterSheetWriter(character)
    writer.write_to_PDF(args.infile, args.outfile)
