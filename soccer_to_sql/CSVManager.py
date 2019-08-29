"""
Manager class to handle csv file storage of scraped data
"""
import csv

CSV_FILENAME = "oddsportal.csv"


class CSVFileMangager:
    def __init__(self):
        """
        initialize csv_file writer
        """

        self.csv_file = open(CSV_FILENAME, mode='w')
        self.csv_file_writer = csv.writer(self.csv_file, delimiter=',')


    def add_soccer_match(self, league, retrieved_from_url, match):
        """
        Insert a soccer match entry into the database.

        Args:
            league (dict): The dict result from parsing a league.json file.

            retrieved_from_url (str): URL this match was retrieved from.

            match (object): The SoccerMatch to insert into the database.
        """

        # write row into csv file
        self.csv_file_writer.writerow([
            league["league"],
            league["area"],
            retrieved_from_url,
            str(match.get_start_time_unix_int()),
            str(match.get_end_time_unix_int()),
            match.get_team1_string(),
            match.get_team2_string(),
            match.get_outcome_string(),
            str(match.get_team1_odds()),
            str(match.get_team2_odds()),
            str(match.get_draw_odds()),
            str(match.get_team1_score()),
            str(match.get_team2_score())


        ])

    def __del__(self):
        """
        Destructor.
        """

        self.csv_file.close()



