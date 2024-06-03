<?php
// Параметры подключения к базе данных
$servername = "db";
$username = "root";
$password = "helloworld";
$dbname = "web";

// Создание подключения
$conn = new mysqli($servername, $username, $password, $dbname);

// Проверка подключения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Получение данных из формы, если они были отправлены
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $category = $_POST['category'];
    $title = $_POST['title'];
    $description = $_POST['description'];

    // Подготовленный запрос для добавления объявления в базу данных
    $stmt = $conn->prepare("INSERT INTO ad (email, category, title, description) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $email, $category, $title, $description);
    $stmt->execute();

    echo "Объявление успешно добавлено в базу данных";

    // Закрытие подготовленного запроса
    $stmt->close();
}

// Закрытие подключения
$conn->close();
?>
