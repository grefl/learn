#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isValidWalk(const char *walk) {
  if (strlen(walk) != 10) return false;
  int horizontal = 0;
  int vertical   = 0;

  for (int i = 0; i < 10; i +=1) {
    char c = walk[i];
    if (c == 'n')
      vertical +=1;
    else if (c == 's')
      vertical -=1;
    else if (c == 'w')
      horizontal +=1;
    else
      horizontal -=1;
  }
  return vertical == 0 && vertical == horizontal;
}


int main() {
  bool is_valid = isValidWalk("nsnsnsnsns");
  printf("%d \n", is_valid);
}
