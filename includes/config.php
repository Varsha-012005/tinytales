<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
$host = 'localhost';
$db   = 'tiny_tales';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Application settings
define('MAX_WORD_COUNT', 1000);
define('MIN_WORD_COUNT', 50);
define('DEFAULT_WORD_COUNT', 100);
define('EXPORT_PATH', __DIR__ . '/exports/');

// Create exports directory if it doesn't exist
if (!file_exists(EXPORT_PATH)) {
    mkdir(EXPORT_PATH, 0755, true);
}

session_start();

// Initialize user preferences if logged in
if (isset($_SESSION['user_id'])) {
    $stmt = $pdo->prepare("SELECT * FROM user_preferences WHERE user_id = ?");
    $stmt->execute([$_SESSION['user_id']]);
    $_SESSION['prefs'] = $stmt->fetch() ?: [
        'dark_mode' => false,
        'default_word_count' => DEFAULT_WORD_COUNT,
        'default_genre' => null
    ];
}
?>