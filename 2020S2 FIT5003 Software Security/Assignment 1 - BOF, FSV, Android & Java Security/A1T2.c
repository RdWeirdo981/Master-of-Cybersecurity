# include < stdio.h >
  # include < stdlib.h >
  # include < string.h >
  # include < unistd.h >
  # include < sys / socket.h >
  # include < netinet / ip.h >
  void myprintf(char * msg) {
    char dummy[DUMMY_SIZE];
    memset(dummy, 0, DUMMY_SIZE);
    printf("%s",msg);  
  }
int check_authentication(char * username, char * password) {
  char password_buffer[BUF_SIZE];
  int auth_flag[1];
  auth_flag[0] = 0;
  strncpy(password_buffer, password);
  printf(" checking  the   following    username : ");
  myprintf(username);
  if (strcmp(password_buffer, " passwd1 ") == 0 & strcmp(username, " user1 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd2 ") == 0 & strcmp(username, " user2 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd3 ") == 0 & strcmp(username, " user3 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd4 ") == 0 & strcmp(username, " user4 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd5 ") == 0 & strcmp(username, " user5 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd6 ") == 0 & strcmp(username, " user6 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " passwd7 ") == 0 & strcmp(username, " user7 ") == 0)
    auth_flag[0] = 1;
  if (strcmp(password_buffer, " admino ") == 0 & strcmp(username, " admin ") == 0)
    auth_flag[0] = 1;
  return auth_flag[0];
}
int main(int argc, char * argv[]) {
  int result = 0;
  FILE * fp;
  char buff[255];
  if (argc < 3) {
    printf(" Usage : %s <username > <  password >\n", argv[0]);
    exit(0);
  }
  result = check_authentication(argv[1], argv[2]);
  if (result != 0) {
    printf("\n -= -= -= -= -= -= -= -= -= -= -= -= -= -\n");
    printf("       Access   Granted .\n");
    printf(" -= -= -= -= -= -= -= -= -= -= -= -= -= -\n");
    fp = fopen("./ fit5003 . txt", "r");
    fgets(buff, 255, (FILE * ) fp);
    printf(" secret   data : %s\n", buff);
    fclose(fp);
  } else {
    printf("\ nAccess   Denied .\n");
  }
}