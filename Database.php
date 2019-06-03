<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Database
 *
 * @author subbu
 */
class Database {
    //put your code here
    private $host      = DB_HOST;
    private $user      = DB_USER;
    private $pass      = DB_PASS;
    private $dbname    = DB_NAME;
 
    private $dbh;
    private $error;
    private $stmt;
    
    private static $_instance = null;
 
    public function __construct(){
        //$db = self::get_instance();
        //$db->connectdb();
        //return $db;
        $this->connectdb();
    }
    
    
    private function connectdb(){
         // Set DSN
        $dsn = 'mysql:host=' . $this->host . ';dbname=' . $this->dbname;
        // Set options
        $options = array(
            PDO::ATTR_PERSISTENT    => true,
            PDO::ATTR_ERRMODE       => PDO::ERRMODE_EXCEPTION
        );
        // Create a new PDO instanace
        try{
            $this->dbh = new PDO($dsn, $this->user, $this->pass, $options);
        }
        // Catch any errors
        catch(PDOException $e){
            $this->error = $e->getMessage();
            echo $e->getMessage();
        } 
    }
    
    
    
    public static function get_instance(){
        if(!isset(self::$_instance)){
           self::$_instance = new Database();
        }
        return self::$_instance;
    }
    
    /*
     * 
     * 
     */
    public function query($query){
            // echo "<br/>q = ".$query."<br/>";
             $this->stmt = $this->dbh->prepare(strip_tags($query));
            // var_dump($this->stmt);
    }
    
    /*
     * 
     */
            public function bind($param, $value, $type = null){
            if (is_null($type)) {
                switch (true) {
                    case is_int($value):
                        $type = PDO::PARAM_INT;
                        break;
                    case is_bool($value):
                        $type = PDO::PARAM_BOOL;
                        break;
                    case is_null($value):
                        $type = PDO::PARAM_NULL;
                        break;
                    default:
                        $type = PDO::PARAM_STR;
                }
            }
            $this->stmt->bindValue($param, $value, $type);
        }
        
        /*
         * 
         */
        public function execute(){
            try{
            $return  = $this->stmt->execute();
           // var_dump($this->stmt->errorInfo());
            return $return;
             } catch(PDOException $e){
            $this->error = $e->getMessage();
              echo $e->getMessage();
            }
           
        }
        
        /*
         * 
         * 
         */
        public function resultset(){
            $this->execute();
            return $this->stmt->fetchAll(PDO::FETCH_OBJ);
        }
        
        /*
         * 
         */
        public function single(){
            $this->execute();
            return $this->stmt->fetch(PDO::FETCH_OBJ);
        }
        
        /*
         * 
         */
        public function rowCount(){
            return $this->stmt->rowCount();
        }
        
        /*
         * 
         */
       public function lastInsertId(){
            return $this->dbh->lastInsertId();
        }

    
}
