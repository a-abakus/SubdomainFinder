# Subdomain Finder
A simple Python script to find subdomains using a wordlist.

## Introduction
Subdomain Finder is a Python script that allows you to discover subdomains of a given domain by using a wordlist. It utilizes DNS resolution to check if subdomains exist for the specified domain.

## Usage
```
pip3 install -r requirements.txt

python3 subdomain_finder.py <example.com> <subdomainlist>
```

## Example

```
$ python3 subdomain_finder.py example.com /path/to/wordlist.txt
 ___      _        _                _        ___ _         _         
/ __|_  _| |__  __| |___ _ __  __ _(_)_ _   | __(_)_ _  __| |___ _ _ 
\__ \ || | '_ \/ _` / _ \ '  \/ _` | | ' \  | _|| | ' \/ _` / -_) '_|
|___/\_,_|_.__/\__,_\___/_|_|_\__,_|_|_||_| |_| |_|_||_\__,_\___|_|

 Found subdomain1.example.com
 Found subdomain2.example.com
 ...
```
