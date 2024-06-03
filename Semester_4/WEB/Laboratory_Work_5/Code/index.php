<!DOCTYPE html>
<html>
<head>
    <title>Объявления</title>
</head>
<body>

<h2>Добавить объявление</h2>
<form action="add_advertisement.php" method="post">
    Email: <input type="text" name="email"><br>
    Категория: <input type="text" name="category"><br>
    Заголовок: <input type="text" name="title"><br>
    Описание: <textarea name="description"></textarea><br>
    <input type="submit" value="Добавить">
</form>

<h2>Список объявлений</h2>
<?php
include 'config.php';

// Подключение к базе данных
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверка подключения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Запрос для выборки всех объявлений из базы данных
$sql = "SELECT * FROM ad";
$result = $conn->query($sql);

// Вывод результатов запроса
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "Email: " . $row["email"]. " - Категория: " . $row["category"]. " - Заголовок: " . $row["title"]. " - Описание: " . $row["description"]. "<br>";
    }
} else {
    echo "В базе данных нет объявлений";
}

// Закрытие подключения
$conn->close();
?>
</body>
</html>
