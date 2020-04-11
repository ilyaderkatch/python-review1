Реализация игры быки и коровы

Начало игры: ввод имени. Под этим именем результаты будут вноситься в рейтинговую таблицу

Функционал:  
Ввод/вывод через консоль
Игроку буде предложено два типа игры:  
1. Угадывать число компьютера 
2. Загадать число компьютеру  
В первом случае по достижении загаданного числа результаты игрока будут внесены в рейтинговую таблицу.  
Во втором случае компьютер будет расчитывать оптимальный вопрос для угадывания числа и, соответсвенно, угадывать число(гарантируется, что количество вопросов от компьютера бует не более чем семь). Важно: на первом шаге возможен долгий анализ нового запроса, однако гарантируется, что в худшем случае компьютер отвечает менее через 30 секунд.

Вспомогательный функционал: 
1. В первом режиме можно закончить игру досрочно, в этом случае будет выведено загаданное число.
2. Вызов рейтинговой таблицы. Будет выведена рейтинговая таблица по увелечению попыток в формате место-имя-попытки
   Рейтинг сохраняется и после завершения кода, тк хранится в отдельном файле в папке с исходником игры.
3. Удаление рейтинга. В этом случае удаляются все предыдущие записи в таблице.

Кроме всего перечисленного обработаны все исключения по вводу с клавиатуры

В обновленной версии:
1. Результаты записываются в бинарный файл
2. Теперь можно выбрать количество цифр в загадываемом(в двух режимах) числе.  
Отдельный комметарий для режима загадывания числа: для числа из 4 цифр продолжает работать умное отгадывание, для большего числа сделано "тупое" отгадывание, тк алгоритм умного работает крайне долго, отсюда увеличивается количество вопросов от компьютера. Помимо этого для чисел из 9 и 10 цифр алгоритм отгадывания долгий - это связано с небыстрой генерацией списка возможных чисел в самом начале
