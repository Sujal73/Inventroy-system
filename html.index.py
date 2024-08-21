<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Product Management System</h1>
            <nav>
                <button onclick="showSection('admin')">Admin</button>
                <button onclick="showSection('user')">User</button>
            </nav>
        </header>
        <main>
            <section id="admin-section" class="hidden">
                <h2>Admin Actions</h2>
                <button onclick="fetchProducts()">Display All Products</button>
                <button onclick="fetchSpecificProduct()">Display Specific Product</button>
                <button onclick="addProduct()">Add New Product</button>
                <button onclick="updateProduct()">Update Product</button>
                <button onclick="deleteProduct()">Delete Product</button>
                <button onclick="fetchUserReports()">Display User Reports</button>
                <div id="admin-results"></div>
            </section>
            <section id="user-section" class="hidden">
                <h2>User Actions</h2>
                <button onclick="fetchProducts()">Display All Products</button>
                <button onclick="fetchSpecificProduct()">Display Specific Product</button>
                <button onclick="fetchUserBills()">Display My Bills</button>
                <button onclick="buyProduct()">Buy Product</button>
                <div id="user-results"></div>
            </section>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>
