# Live Power Data from the ISS

This webpage (spartan-scraper.html) populates the table below with real-time power data, pulled from the "ISS Live" server. Specifically, it interfaces with the Station, Power Articulation and Control (SPARTAN) Photovoltaic Control Unit (PVCU) to capture the drive voltages, drive currents, and beta gimbal assembly (BGA) positions for each of the 8 solar arrays on the ISS. It can be used to log power generation and consumption in order to get a better understanding of the Station's power behavior as it orbits around planet Earth. For a more graphical representation of this data, visit the SPARTAN Power Console Display.

The first row of the table is the "live" data. It changes as soon as a value is updated from the ISS Live server. Click on the 'Start Logging' button to begin logging. For each logging interval (specified by the input textbox below), a snapshot of the data is appended to the table (rows will be sorted ascendingly by time). The table can then be exported to a CSV file for further analysis by clicking on the 'Export Table to CSV' hyperlink.

Additional fields for the ISS orbital position are now included. See ADCO Orbital Position Display for more information. This data seems to be published once every 10 seconds.

Note: Your data log may contain stale data. Make sure you have a stable Internet connection to connect to the ISS Live server. And be ready for any intermittent "no signal" connectivity issues with the ISS.
