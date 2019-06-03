<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

define("DB_HOST", "localhost");
define("DB_USER", "root");
define("DB_PASS", "root@kms");
define("DB_NAME", "chatbot");
include 'Database.php';

$db = new Database();
$sql = "SELECT * FROM faqtab";
$db->query($sql);
$data = $db->resultset();
$jobj = new stdclass();
$jobj->intents = [];
foreach($data as $key=>$obj){
    
    $newobj = new stdclass();
    $newobj->tag = $obj->tagname;
    $newobj->patterns = explode("##",$obj->qas);
    $newobj->responses = explode("##",$obj->answer);
    $newobj->context_set = $obj->contex;
    $jobj->intents [] = $newobj;  
	//var_dump($newobj->patterns);

}

$fp = fopen('/var/www/html/raju/json/results.json', 'w');
fwrite($fp, json_encode($jobj));
fclose($fp);
