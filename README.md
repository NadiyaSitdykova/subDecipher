subDecipher
==========
Скрипты написаны на python3.

main запускать с параметрами:

-q {sentences_count} — для простого запуска алгоритма шифровки и последующей дешифровки случайных sentences_count предложений из brown.corpus.

пример: ```python main.py -q 10```

или

-l {iterations_count} — для подсчета статистики для выборок 5-20 случайных предложений по iterations_count (число запусков алгоритма) для каждого числа предложений.

пример: ```python main.py -l 20```

plotting.py чертит график по ранее собранной мной статистике c iterations_count = 20. Статистика также хранится в plotting.py в листе results. Где числа в листе означают среднее число верно подобранных букв в ключе в результате <iterations_count> запусков алгоритма. Аналогичную статистику можно собрать запустив main с параметром -l <iterations_count>