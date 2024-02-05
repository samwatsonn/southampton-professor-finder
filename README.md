
# Southampton Professor Finder

This script can be used to search the entire University of Southampton
staff directory for specific research terms. 

This may be helpful for finding researchers working in specific areas for prospective
dissertation, masters, or PhD students.

## How To Use

1. Clone the repository
```angular2html
git clone 
```
2. Setup Python environment
```angular2html
pip install -r requirements.txt

// Windows
./venv/Scripts/activate

// Mac
source venv/bin/activate
```
3. Updates TERMs in `professor_finder.py`.
```python
TERMS = [
    "YOUR SEARCH TERM HERE",
    "ANOTHER SEARCH TERM",
]
```
4. Run the script
```angular2html
python professor_finder.py
```

## Updating the cached Staff Directory
To enable faster searching, the script caches the 
staff pages in the `data` directory. Last updated on 04-02-2024.

To update the cache, simply uncomment the following line in `professor_finder.py`:
```python
# get_people()
```
Then run the script as normal. This will update the cache with the latest staff directory.

## Examples````
```angular2html
NATURAL LANGUAGE PROCESSING
 - [9x] Doctor Stuart Middleton (https://www.southampton.ac.uk/people/5wzm8c/doctor-stuart-middleton)
 - [2x] Doctor Rafael Mestre (https://www.southampton.ac.uk/people/5ylbc9/doctor-rafael-mestre)
 - [2x] Miss Zhiying Ben (https://www.southampton.ac.uk/people/5y5pfp/miss-zhiying-ben)
 - [2x] Mr Lingzhi Shen (https://www.southampton.ac.uk/people/62bsf2/mr-lingzhi-shen)
 - [2x] Mr Gyanendro Loitongbam (https://www.southampton.ac.uk/people/5zbfm5/mr-gyanendro-loitongbam)
 - [1x] Mr Mohammed Mosuily (https://www.southampton.ac.uk/people/5zl7zv/mr-mohammed-mosuily)
 - [1x] Professor Jonathon Hare (https://www.southampton.ac.uk/people/5x2nft/professor-jonathon-hare)
 - [1x] Doctor Craig Webber (https://www.southampton.ac.uk/people/5wy8qq/doctor-craig-webber)
 - [1x] Doctor George Konstantinidis (https://www.southampton.ac.uk/people/5xlfwx/doctor-george-konstantinidis)
 - [1x] Doctor Kate Farrahi (https://www.southampton.ac.uk/people/5xkhzr/doctor-kate-farrahi)
 - [1x] Mrs Verity Ward (https://www.southampton.ac.uk/people/5xmzmt/mrs-verity-ward)
 - [1x] Mr Conor Gaughan (https://www.southampton.ac.uk/people/5ywhlt/mr-conor-gaughan)
 - [1x] Doctor Shoaib Jameel (https://www.southampton.ac.uk/people/5zdg5y/doctor-shoaib-jameel)
 - [1x] Doctor Jennifer Williams (https://www.southampton.ac.uk/people/5zc9gl/doctor-jennifer-williams)
 - [1x] Ms Jayati Deshmukh (https://www.southampton.ac.uk/people/65clnm/ms-jayati-deshmukh)
```
Results are ordered by the number of times the search term appears on the staff member's page.
```angular2html
CANCER IMMUNOTHERAPY
 - [4x] Professor Mark Cragg (https://www.southampton.ac.uk/people/5wz2dl/professor-mark-cragg)
 - [4x] Professor Aymen Al Shamkhani (https://www.southampton.ac.uk/people/5wy7nw/professor-aymen-al-shamkhani)
 - [3x] Doctor Ali Roghanian (https://www.southampton.ac.uk/people/5x6fr7/doctor-ali-roghanian)
 - [2x] Doctor Claude Chan (https://www.southampton.ac.uk/people/5wzddb/doctor-claude-chan)
 - [2x] Professor Gareth Thomas (https://www.southampton.ac.uk/people/5x6d5l/professor-gareth-thomas)
 - [2x] Miss Josephine Buckingham (https://www.southampton.ac.uk/people/5xfw5j/miss-josephine-buckingham)
 - [2x] Professor Sean Lim (https://www.southampton.ac.uk/people/5x6fmh/professor-sean-lim)
 - [1x] Doctor Silvia Redondo Garcia (https://www.southampton.ac.uk/people/62fc9m/doctor-silvia-redondo-garcia)
 - [1x] Doctor Diana Garay Baquero (https://www.southampton.ac.uk/people/5xrhzb/doctor-diana-garay-baquero)
 - [1x] Doctor Kirstie Cleary (https://www.southampton.ac.uk/people/5xg8cp/doctor-kirstie-cleary)
 - [1x] Mr Timo Kuerten (https://www.southampton.ac.uk/people/5xth6x/mr-timo-kuerten)
 - [1x] Professor Juliet Gray (https://www.southampton.ac.uk/people/5wzptx/professor-juliet-gray)
 - [1x] Professor Stephen Beers (https://www.southampton.ac.uk/people/5wzmb7/professor-stephen-beers)
 - [1x] Professor Eugene Healy (https://www.southampton.ac.uk/people/5wz6fg/professor-eugene-healy)
 - [1x] Doctor Salah Mansour (https://www.southampton.ac.uk/people/5x5zk5/doctor-salah-mansour)
```