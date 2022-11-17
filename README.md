# Wordpress Fuzz
Python tool for fuzzing Wordpress websites.

![Basic Usage](wp-fuzz.png)

## Instalation

``` 
pip install requests
curl https://raw.githubusercontent.com/entr0pie/wordpress-fuzz/main/wp-fuzz.py | tee wp-fuzz.py
```


## Usage
```
python3 wp-fuzz.py --host=http://your-blog.com/
python3 wp-fuzz.py --host=http://your-blog.com/ --wordlist=my-wordlist.txt
```

## Filtering Results
```
cat wordpress-fuzz.txt | fgrep -n "ok"  # 200 status code links.
cat wordpress-fuzz.txt | fgrep -nv "ok" # Pages that exist, but maybe aren't accesible.
cat wordpress-fuzz.txt | fgrep -n "403" # Forbidden pages.
```
