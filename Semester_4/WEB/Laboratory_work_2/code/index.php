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

$sixty_four = 8 ** 2;
echo "$sixty_four<br>";

$my_num = 666;
$answer = $my_num;
$answer += 2;
$answer *= 2;
$answer -= 2;
$answer /= 2;
$answer -= $my_num;
echo "Переменная answer = $answer, задание выполнено верно<br>";

$a=10;
$b=3;
$remainder = $a % $b;
echo "Остаток от деления $a на $b = $remainder <br>";
if ($remainder == 0) {
    echo "Делится:";
    $ab = $a / $b;
    echo " $a / $b=$ab<br>";
} else {
    echo "Делится с остатком $remainder<br>";
}

$st = pow(2, 10);
$sqrt = sqrt(245);
$mas = [4, 2, 5, 19, 13, 0, 10];
$sum = 0;
foreach ($mas as $i) {
    $sum += pow($i,2);
}
$sum = sqrt($sum);
echo "2^10 = $st; квадратный корень из 245 = $sqrt<br>";
echo "Корень из суммы квадратов элементов массива = $sum<br>";

$sqrt1 = round(sqrt(379));
$sqrt2 = round(sqrt(379), 1);
$sqrt3 = round(sqrt(379), 2);
$sqrt_of_587 = [];
$sqrt_of_587['floor'] = floor(sqrt(579));
$sqrt_of_587['ceil'] = ceil(sqrt(579));

echo "квадратный корень из 379 = $sqrt1 = $sqrt2 = $sqrt3 <br>";
echo "квадратный корень из 587 = {$sqrt_of_587['floor']}= {$sqrt_of_587['ceil']} <br>";

$min = min(4, -2, 5, 19, -130, 0, 10);
$max = max(4, -2, 5, 19, -130, 0, 10);
echo "Минимальное: $min; максимальное: $max<br>";

$random = rand(1, 100);
echo "Случайно число от 1 до 100: $random <br>";

$mas_for_random = [];
foreach (range(0, 9) as $i) {
    $mas_for_random[] = rand(1, 10000);
    echo "$mas_for_random[$i] ";
}
echo "<br>";

$module1 = abs($a - $b);
$module2 = abs(($a = 24) - ($b = 12));
echo "Работа с модулем:$module1; $module2 <br>";

$mas = [1, 2, -1, -2, 3, -3];
foreach (range(0, count($mas) - 1) as $i) {
        $mas[$i] = abs($mas[$i]);
        echo "$mas[$i] ";
}
echo "<br>";


$mas_for_dividers = [];
$number = 30;
echo "Делители $number:";
foreach (range(1, $number) as $i) {
    if ($number % $i== 0) {
        $mas_for_dividers[] = $i;
    }
}
foreach ($mas_for_dividers as $i) {
    echo $i . " ";
}
echo "<br>";

$sumElementsArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$count = 0;
$sum = 0;
foreach ($sumElementsArray as $i) {
    $sum += $i;
    $count++;
    if ($sum > 10) {
        break;
    }
}
echo "Надо сложить первые $count чисел <br>";

// Don't change the line below
echo "\nYour order is: $very_bad_unclear_name.";
