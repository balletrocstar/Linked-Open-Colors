<?php header("Content-Type: application/rdf+xml; UTF-8");
echo '<?xml version="1.0" encoding="utf-8"?>'; ?>
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:loco="http://loc.moreways.net/loco#"
    xml:lang="en"
>

  <foaf:Document rdf:about="http://loc.moreways.net/color/<? echo $_GET['color']; ?>.rdf">
    <foaf:primaryTopic rdf:resource="http://loc.moreways.net/color/<? echo $_GET['color']; ?>"/>
  </foaf:Document>

  <loco:Color rdf:about="http://loc.moreways.net/color/<? echo $_GET['color']; ?>">
    <rdfs:label>#<? echo $_GET['color']; ?></rdfs:label>
    <foaf:page rdf:resource="http://loc.moreways.net/color/<? echo $_GET['color']; ?>.html" />
  </loco>
  
</rdf:RDF>

