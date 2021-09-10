import sqlite3

#Подключение базы данных (для примера используется sqlite3, так как в стандратном наборе Python)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

#Вариант 1 - "злостный читатель" тот, кто много читает
cursor.execute('''
	SELECT s.name 
		FROM (
			SELECT bo.student_id, COUNT(bo.student_id) AS count_
        		FROM borrow AS bo
        		GROUP BY bo.student_id)
    	JOIN student AS s
    	WHERE count_ = (
    		SELECT MAX(count_) FROM (SELECT bo.student_id, COUNT(bo.student_id) AS count_
        		FROM borrow AS bo
        		GROUP BY bo.student_id)) AND s.id = student_id;
			''')

student_list = cursor.fetchall()
print('Самые читающие студенты')
print(student_list)

#Вариант 2 - "злостный читатель" тот, кто не вовремя сдал книгу
cursor.execute('''
	SELECT s.name 
		FROM (
			SELECT bo.student_id, bo.borrow_date, bo.return_date
        		FROM borrow AS bo
        		WHERE return_date - borrow_date > time)
    	JOIN student AS s
    	WHERE s.id = student_id
    	GROUP BY s.id;
			''')

student_list = cursor.fetchall()
print('Не сдающие книги вовремя студенты')
print(student_list)

#Вариант 3 - "злостный читатель" тот, кто не сдал книгу, хотя срок уже прошел   
cursor.execute('''
    SELECT s.name 
        FROM (
            SELECT bo.student_id, bo.borrow_date, bo.return_date
                FROM borrow AS bo
                WHERE return_date = 'None'
                AND CURDATE() - borrow_date > time
                )
        JOIN student AS s
        WHERE s.id = student_id
        GROUP BY s.id;
            ''')

student_list = cursor.fetchall()
print('Не сдающие книги вовремя студенты')
print(student_list)

conn.close()