<?php

// Проверяем наличие данных в $_POST
if (isset($_POST['email']) && isset($_POST['title']) && isset($_POST['text']) && isset($_POST['category'])) {
    // Получаем данные из POST запроса
    $email = $_POST['email'];
    $title = $_POST['title'];
    $text = $_POST['text'];
    $category = $_POST['category'];

    // Функция для добавления записи в Google Таблицу
    addEntryToGoogleSheet($email, $title, $text, $category);
} else {
    echo 'Все поля формы должны быть заполнены!';
    exit(); // Прерываем выполнение скрипта, чтобы избежать дальнейшей обработки
}

require_once "vendor/autoload.php";

use Google\Spreadsheet\DefaultServiceRequest;
use Google\Spreadsheet\ServiceRequestFactory;

// Инициализация клиента Google Sheets API
function initializeGoogleClient()
{
    $client = new Google_Client();
    $client->setApplicationName('Google Sheets API PHP');
    $client->setScopes(Google_Service_Sheets::SPREADSHEETS);
    $client->setAccessType('offline');
    $client->setAuthConfig('C:\web labs\weblab4-420618-1f07ab7f67b7.json');
}

// Функция для записи данных в Google Таблицу
function addEntryToGoogleSheet($email, $title, $text, $category, $client){
    $service = new Google_Service_Sheets($client);

    $spreadsheetId = '1lr2su0KF6Afbst5C6KrnmH-dQqsosK4WAxF8ZvkcSWM/edit#gid=0';
    $range = 'Sheet1'; // Название листа в таблице

    $values = [
        [$email, $title, $text, $category]
    ];

    $body = new Google_Service_Sheets_ValueRange([
        'values' => $values
    ]);

    $params = [
        'valueInputOption' => 'RAW'
    ];

    $result = $service->spreadsheets_values->append($spreadsheetId, $range, $body, $params);
    if ($result->getUpdates()->getUpdatedCells() > 0) {
        echo 'Объявление успешно добавлено!';
    } else {
        echo 'Произошла ошибка при добавлении объявления';
    }
}

// Получаем данные из POST запроса
$email = $_POST['email'];
$title = $_POST['title'];
$text = $_POST['text'];
$category = $_POST['category'];

// Инициализируем клиент Google Sheets API
$client = initializeGoogleClient();

// Добавляем запись в Google Таблицу
addEntryToGoogleSheet($email, $title, $text, $category);