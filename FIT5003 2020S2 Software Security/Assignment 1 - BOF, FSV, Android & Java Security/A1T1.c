#include <stdio.h>

#include <stdlib.h>

#include <unistd.h>

#include <string.h>

#include <sys/socket.h>

#include <netinet/ip.h>

#define PORT 7070
int exec_command(int sock, char * buf) {
  char command[300];
  // redirecting the stdout to the socket
  close(STDOUT_FILENO);
  dup2(sock, STDOUT_FILENO);
  // The following line is different for each linux command to be executed.
  sprintf(command, "/usr/bin/nslookup %s", buf);
  // validation check
  int is_cmd = strchr(command, ';');
  // if thers is a ";", strchr will return NULL
  // another method: compare to see if command is nslookup
  // int is_cmd = strncmp("/usr/bin/nslookup", command, 17);
  if (is_cmd != NULL) {
    system(command);
  } else {
    printf("Invalid Input!");
  }
  return 0;
}


  
void main() {
  struct sockaddr_in server;
  struct sockaddr_in client;
  int clientLen;
  int sock, newsock;
  char buf[1500];
  pid_t pid, current = getpid();
  int ret_val;
  sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (sock < 0) {
    perror("Error opening socket");
    exit(1);
  }
  memset((char * ) & server, 0, sizeof(server));
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = htonl(INADDR_ANY);
  server.sin_port = htons(PORT);
  ret_val = bind(sock, (struct sockaddr * ) & server, sizeof(server));
  if (ret_val < 0) {
    perror("ERROR on binding");
    exit(1);
  }
  listen(sock, 5);
  clientLen = sizeof(client);
  while (1) {
    newsock = accept(sock, (struct sockaddr * ) & client, & clientLen);
    if (newsock < 0) {
      perror("Error on accept");
      exit(1);
    }
    if (fork() < 0) {
      perror("Error on fork");
      close(sock);
      exit(1);
    }
    pid = getpid();
    // printf("child pid for new connectin %d", pid);
    if (pid == current) {
      continue;
    } else {
      bzero(buf, 1500);
      recvfrom(newsock, buf, 1500 - 1, 0, (struct sockaddr * ) & client, & clientLen);
      exec_command(newsock, buf);
      close(newsock);
      exit(0);
    }
  }
  close(sock);
}