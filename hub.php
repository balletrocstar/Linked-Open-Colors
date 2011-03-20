<?php

error_reporting(0);

function get_color() {
    $color = $_GET["color"];
    //$color = strtolower($color);
    return $color;
}

function get_suffix() {
    require_once "inc/conNeg/conNeg.inc.php";
    $mimeBest = conNeg::mimeBest();
    $equivalences = array(
                        "text/html"             => "html",
                        "application/xhtml+xml" => "html",
                        "application/rdf+xml"   => "rdf",
                        "text/rdf+n3"           => "rdf",
                        "text/turtle"           => "rdf",
                        "application/x-turtle"  => "rdf"
                        
                    );
    if (array_key_exists($mimeBest, $equivalences)) {
        return $equivalences[$mimeBest];
    } else {
        return "html";
    }
}

function redirect($color, $suffix) {
    header("HTTP/1.1 303");
    header("Vary: Accept");
    header("Location: http://loc.moreways.net/color/" . $color . "." . $suffix);
}

redirect(get_color(), get_suffix());

?>

