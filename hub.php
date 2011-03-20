<?php

function get_suffix() {
    require_once "inc/conNeg/conNeg.inc.php";
    $charsetBest = conNeg::charBest();
    return $charsetBest; //FIXME: convert from charset to suffix
}

$color = $_GET["color"];
$suffix =get_suffix();

echo $color . " as " . $suffix;

?>

