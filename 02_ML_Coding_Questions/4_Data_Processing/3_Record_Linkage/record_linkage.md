# Record Linkage

  As a data analyst for a mergers and acquisitions firm, your services have been
  requested in a potential buyout of Spotify by YouTube. Stakeholders at YouTube Music
  would like a list of existing Spotify premium users who already have YouTube Music
  premium. This will help establish a fairer acquisition price.

  Consider the following dataframe provided by YouTube:

+----+--------------+-------------+----------------------------------+--------------------+--------------------+--------------------------------------+
|    | first_name   | last_name   | preferred_contact                |   last_four_digits |   billing_zip_code | non_mfa_ip_addresses                 |
|----+--------------+-------------+----------------------------------+--------------------+--------------------+--------------------------------------|
|  0 | Sutton       | Duke        | sutt-duke@progressenergyinc.info |               7868 |              14661 | ['57.44.245.252', '227.226.40.165']  |
|  1 | Zisel        | Bolding     | zi-bo@acusage.net                |               2770 |              42080 | ['26.134.133.30', '129.5.121.157']   |
|  2 | Mac          | Saulsberry  | masaulsber@acusage.net           |               8724 |              18555 | ['142.195.32.205', '133.9.249.53']   |
|  3 | Sonny        | Werth       | sonn.wer@diaperstack.com         |               4787 |              73432 | ['60.212.20.208', '134.151.216.140'] |
|  4 | Amir         | Grondin     | am.gro@arketmay.com              |               3360 |              75736 | ['98.86.27.1', '15.186.111.73']      |
# ...
# More of the same kind of data.

  It represents information about each premium YouTube subscription owner and
  is referenced as `df_youtube`.

  Consider the other dataframe provided by Spotify:

+----+--------------+-------------+---------------------------------+--------------------+--------------------+-------------------------------------+
|    | first_name   | last_name   | preferred_contact               |   last_four_digits |   billing_zip_code | non_mfa_ip_addresses                |
|----+--------------+-------------+---------------------------------+--------------------+--------------------+-------------------------------------|
|  0 | Judd         | Catlin      | jucatli@diaperstack.com         |               1155 |              33162 | ['230.5.51.135', '158.201.151.245'] |
|  1 | Gerlinde     | Francis     | gerlindefr@arvinmeritor.info    |               2577 |              97632 | ['6.195.240.222', '64.233.118.244'] |
|  2 | Laris        | Pires       | lari-pir@progressenergyinc.info |               9125 |              79598 | ['9.169.26.141', '29.148.241.26']   |
|  3 | Damiana      | Orme        | damiaorme@arvinmeritor.info     |               8380 |              55324 | ['140.57.106.48', '45.210.102.173'] |
|  4 | Wayde        | Dang        | wayd-dang@acusage.net           |               3719 |              21462 | ['243.102.133.47', '250.95.189.48'] |
# ...
# More of the same kind of data.

  It represents information about each premium Spotify subscription owner and
  is referenced as `df_spotify`.

  Find and return the YouTube Pandas dataframe with only the entires of overlapping 
  subscribers to both YouTube premium and Spotify premium. Overlap is defined as:

  • Match on preferred contact

  • Match on first and last name, last 4 digits of the payment instrument, and 
    the billing zip code

  • Match on first and last name, billing zip code, and the first 3 octets of 
    any non-mfa IP addresses

# Hints

# [Hint_1]

  First, we need to find the indices of matching preferred contacts of the two 
  dataframes.

# [Hint_2]

  Then, we need to find the intersection of the indices with matching first and
  last name, last 4 digits of the payment instrument, and the billing zip code.

# [Hint_3]

  Next, we need to find the intersection of the indices with matching first and
  last name, billing zip code, and the first 3 octets of any non-mfa IP addresses.

# [Hint_4]

  Lastly, we need to create and return a dataframe that contains the union of the
  indices from all the previous hints within the `df_youtube`.
