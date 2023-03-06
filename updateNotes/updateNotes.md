## Packaging

### Ubuntu

Trying to get exe packaging back up and running on my Linux machine. Installed all dependencies
(although `requirements.txt` needs to be updated. It could not find a lot of packages I think need
to add additional channels).

Looking back into the Pyinstaller `.spec` script I removed all the junk that was related to
finding tensorflow binaries. I remember this giving me a lot of trouble when first writing
the program but commenting all of this stuff out and running pyinstaller still produced a working
(working as in the program launched and did not crash) exe file. So I am leaving that stuff
uncommented for now until I find a situation where it seems to be required.


### Windows

Download Windows 11 virtual machine for Virtual Box. It seems like [Wix](https://wixtoolset.org/docs/wix3/)
is generally what people use to package for windows and is good for automation so going to
try that out. 



## Cocktail version 21 update

Added version 21 membrane and soluble cocktail specifications to the `src/data/cocktail_data` dir.
I also updated the `cocktail_meta.csv` file with the following lines 

```
21_C1536.csv	3/6/2023 -		s
MSC9_1536_cocktail_list_complist.csv	6/6/2023 -		m
```

Dates might need to be changed in the future. 

Need to look back at some of the test data and review how the cocktail assignment was being
determined for each run. 


When attempting to re-run polo after adding new cocktails list program crashes due to out
of bounds exception. Printing out the reagent positions for each csv file along with the
row length gives list like this

```
[3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16] 17
[3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15] 16
```

Something changes with the new cocktail list and rows are shorter by 1 cell.