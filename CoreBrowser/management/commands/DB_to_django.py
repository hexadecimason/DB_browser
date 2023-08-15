# db_name = 'opic_core_django'

# NOTE: BEFORE RUNNING THIS, USE "python manage.py flush" to clear tables.

import pandas as pd
import numpy as np
import django
from psycopg2.extensions import register_adapter, AsIs
import sys, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoreBrowser_config.settings')
django.setup()

sys.path.append('../')
from CoreBrowser.models import Well, Box

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

	def handle(self, *args, **options):
		pass

	# helper function: pandas types and PG types don't interact very well by default
	@staticmethod
	def adapt_np64(val):
		return(AsIs(val))
	register_adapter(np.int64, adapt_np64)

	# PARSE CSV
	master_df = pd.read_csv("C:\\Users\\cull4193\\DB_browser\\CoreBrowser\\management\\commands\\cleaned_data.csv")

	nullboxes_df = pd.read_csv("C:\\Users\\cull4193\\DB_browser\\CoreBrowser\\management\\commands\\nullboxes.csv")	
	nullboxes_df['Box'] = nullboxes_df['Box'].fillna(np.nan).replace([np.nan], None)

	master_df = pd.concat([master_df, nullboxes_df])

	# structure wells with boxes
	print("\nParsing CSV...")
	for file in master_df["File #"].unique():
		print("adding file ", file, "... ", end = '')

		# separate file
		sub_df = master_df[master_df["File #"] == file]

		# create well structure
		well = Well(file_num = file,
	    		api = sub_df['API'].iloc[0],
	    		box_count = 0,
	    		operator = sub_df['Operator'].iloc[0],
	    		lease = sub_df['Lease'].iloc[0],
	    		well_num = sub_df['Well #'].iloc[0],
	    		sec = sub_df['Sec'].iloc[0],
	    		twn = sub_df['Tw'].iloc[0],
	    		twn_d = sub_df['TwD'].iloc[0],
	    		rng = sub_df['Rg'].iloc[0],
	    		rng_d = sub_df['RgD'].iloc[0],
	    		qq = sub_df['Quarter'].iloc[0],
	    		latitude = sub_df['Latitude'].iloc[0],
	    		longitude = sub_df['Longitude'].iloc[0],
	    		county = sub_df['County'].iloc[0],
	    		state = sub_df['State'].iloc[0],
	    		field = sub_df['Field'].iloc[0])

		well.save()

		# add boxes
		count = 0
		for line in range(len(sub_df['File #'])):

			box = Box(file_num_id = file,
					box_num = sub_df['Box'].iloc[line],
					formation = sub_df['Formation'].iloc[line],
					top = sub_df['Top'].iloc[line],
					bottom = sub_df['Bottom'].iloc[line],
					diameter = sub_df['Diameter'].iloc[line],
					box_type = sub_df['Box Type'].iloc[line],
					sample_type = sub_df['Type'].iloc[line],
					condition = sub_df['Condition'].iloc[line],
					restrictions = sub_df['Restrictions'].iloc[line],
					comments = sub_df['Comments'].iloc[line])

			box.save()
			count += 1

		w = Well.objects.get(pk=file)
		w.box_count = count
		w.save()

		print("done")

		#well.save()