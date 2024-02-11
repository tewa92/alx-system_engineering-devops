Command line for the win 
To copy a directory from your local machine to the sandbox environment 
sing SFTP, you typically need to compress the directory into an archive
(e.g., a .zip or .tar file) and then transfer that archive to the sandbox.
Here's how you can do it:

    Compress the directory on your local machine:

    bash

tar -czf directory.tar.gz /path/to/local/directory

Replace /path/to/local/directory with the path to the directory you want
to copy.

Connect to the sandbox using the sftp command:

bash

sftp username@sandbox_host

Replace <username> with your username on the sandbox and <sandbox_host> with
the hostname or IP address of the sandbox.

Once connected, navigate to the directory on the sandbox where you want to
copy the compressed archive.

Use the put command to transfer the compressed archive to the sandbox:

bash

    put directory.tar.gz

    After the file transfer is complete, you can decompress the archive on
the sandbox using the appropriate command (e.g., tar -xzf directory.tar.gz).

Here's an example of the complete process:

bash

tar -czf directory.tar.gz /path/to/local/directory
sftp username@sandbox.example.com
cd /remote/directory/path
put directory.tar.gz
exit

This sequence of commands compresses the directory on your local machine,
connects to the sandbox via SFTP, transfers the compressed archive to the
sandbox, and then exits the SFTP session. Once the file is on the sandbox,
you can decompress it and access its contents as needed.
