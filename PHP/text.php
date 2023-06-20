<?php
class Person {
    public $name;
    public $age;

    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }
}

// 序列化对象
$person = new Person("John", 25);
$serialized = serialize($person);

echo "Serialized: " . $serialized . "\n";

// 反序列化对象
$unserialized = unserialize($serialized);

echo "Name: " . $unserialized->name . "\n";
echo "Age: " . $unserialized->age . "\n";
?>
