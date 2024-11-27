Task 2: Image Encryption Tool

This Python program implements a simple image encryption tool that leverages pixel manipulation techniques. By applying basic mathematical operations to the pixel values, the program is able to encrypt and decrypt images. It is designed to be intuitive, providing users with clear instructions throughout the encryption and decryption processes.
Features

    Image Encryption: Users can encrypt an image by applying a mathematical transformation to each pixel value, effectively modifying the image.
    Image Decryption: The program can reverse the encryption process, restoring the original image.
    Customizable Input: Users can specify both the image file and the encryption key.
    File Handling: The program saves the encrypted and decrypted images to the user-specified file paths.

How It Works

    Encrypt Image: Each pixel value is multiplied by a key and then divided by the key plus one to create the encrypted version of the image.
    Decrypt Image: To recover the original image, the encryption process is reversed by multiplying each pixel value by the key plus one and then dividing by the key.

How to Use

    Run the Program: Start the script to initiate the Image Encryption Tool.
    Choose an Action: Select 'e' for encryption, 'd' for decryption, or 'q' to quit.
    Encrypt Image:
        Enter the encryption key.
        Specify the file path or URL of the image you want to encrypt.
    Decrypt Image:
        Enter the decryption key.
        Provide the location of the encrypted image.
    View Results: The program saves the encrypted and decrypted images, displaying the file paths for easy access.

This code was developed during my internship at The Prodigy Infotech, demonstrating a fundamental approach to image encryption and decryption using pixel manipulation.