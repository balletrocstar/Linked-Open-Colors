<!DOCTYPE html>
<html 
  version="HTML+RDFa 1.1"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:dct="http://purl.org/dc/terms/"
  xmlns:foaf="http://xmlns.com/foaf/0.1/"
  xmlns:sioc="http://rdfs.org/sioc/ns#" 
  lang="en"
>

  <head>
    <title property="dc:title">Linked Open Colors: #<?php echo $_GET["color"]; ?></title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <link rel="transformation" href="http://www-sop.inria.fr/acacia/soft/RDFa2RDFXML.xsl"/>
    <style>
      h1 {
        display: block;
        width: 400px;
        margin: 2em auto auto auto;
        padding: 1em;
        background-color: #ffffff;
        color: #000000;
        font-size: 5em;
        font-weight: bold;
        text-align: center;
      }
      a, a:active, a:visited {
        color: #000000;
        text-decoration: none;
      }
      a:hover {
        color: #000000;
        text-decoration: underline;
      }
    </style>
  </head>

  <body typeof="foaf:Document" about="" style="background-color: #<? echo $_GET['color']; ?>;">

    <h1>
      <a href="http://loc.moreways.net/color/<? echo $_GET['color']; ?>" title="http://loc.moreways.net/color/<? echo $_GET['color']; ?>">
        #<? echo $_GET["color"]; ?>
      </a>
    </h1>

</html>


