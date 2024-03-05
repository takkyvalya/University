<?php
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";


// Write your code here:

$order = &$very_bad_unclear_name;  // нужно сделать присваивание по ссылке
$order .= " very spicy";

echo "$order <br>";

$int1 = 1e4;
$int2 = 5279488;
$float = 4.424;
$No12 = 10;
$no12 = 2;
$HereNo12 = $No12 + $no12;

echo "$int1<br>";
echo "$int2<br>";
echo "$float<br>";
echo "Здесь нет 12: {$HereNo12}<br>";

$lastMonth = 1187.23;
$currentMonth = 1089.98;
$difference = $lastMonth - $currentMonth;
echo "В этом месяце я потратила на $difference долларов больше чем в предыдущем <br>";

$num_languages = 4;
$months = 4;
$days = $months * 16;
$days_per_language = $days / $num_languages;
echo "В среднем, у Мэг ушло $days_per_language дня на изучение каждого языка<br>";

// Don't change the line below
echo "\nYour order is: $very_bad_unclear_name.";
