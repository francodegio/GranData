# GranData

## Description
Repo containing all everything I've done to fulfill the GranData Challenge.

## Installation
### 1. Clone repo

```bash
$ git clone https://github.com/francodegio/GranData.git
```

### 2. Run shell script
This will install the required libraries to download the data and process it with Dask.

```bash
$ cd GranData
$ sh Scripts/setup.sh
```

### 3. Download the data
Dismiss step if you already have the data.

```bash
$ cd Scripts
$ python get_data.py
```

This will download the `tar.gz` files to `./GranData/Data`.
### 4. Unzip
```bash
$ python unzip_files.py
```

