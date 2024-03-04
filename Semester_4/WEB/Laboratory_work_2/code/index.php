<?php
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";


// Write your code here:

$order = &$very_bad_unclear_name;  // нужно сделать присваивание по ссылке
$order .= " very spicy";

echo "$order <br>";

// Don't change the line below
echo "\nYour order is: $very_bad_unclear_name.";