<?php

$equivalences = array(
                    "text/html"             => "html",
                    "application/xhtml+xml" => "html",
                    "application/rdf+xml"   => "rdf",
                    "text/rdf+n3"           => "rdf",
                    "text/turtle"           => "rdf",
                    "application/x-turtle"  => "rdf"
                    
                );

function get_suffix() {
    require_once "inc/conNeg/conNeg.inc.php";
    $mimeBest = conNeg::mimeBest();
    if (array_key_exists($mimeBest, $equivalences)) {
        return $equivalences[$mimeBest];
    } else {
        return "html";
    }
}

$color = $_GET["color"];
$suffix = get_suffix();

echo $color . " as " . $suffix;

?>

