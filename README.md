subDecipher
==========
Scripts are written on  ```python3```.

Run ```main``` with parameters:
* ```-q <sentences_count>``` -- simple run of Cipher algorithm and followin deciphering of ```<sentences_count>``` random sentences from ```brown.corpus```.
Example: ```python3 main.py -q 10```
* ```-l <iterations_count>``` -- computes stats for samples of 5-20 random sentences by ```<iterations_count>``` iterations.
Example: ```python main.py -l 20```

```plotting.py``` draws stats with ```<iterations_count> = 20```. List results in plotting.py contains mean value of correctly found symbols in key after ```<iterations_count>``` iterations. This values also avalilable by running ```main -l <iterations_count>```
