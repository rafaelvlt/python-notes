#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
  int *data;
  int count;
  int cap;
} Stack;

typedef struct
{
  char name[50];
  int val;
} Var;

typedef struct
{
  Var list[100];
  int total;
} Table;

void stack_init(Stack *s);
void push(Stack *s, int val);
int pop(Stack *s);
void stack_clear(Stack *s);
void stack_free(Stack *s);
int get_val(Table *tbl, char *name);
void set_val(Table *tbl, char *name, int val);
int is_num(char *str);

int main()
{
  Stack s;
  Table tbl;
  char line_buf[1024];
  char dest_var[50];
  char *tok;

  // States: 0=wait '=', 1=get var name, 2=process expr
  int state = 0;
  int running = 1;

  stack_init(&s);
  tbl.total = 0;

  while (running && fgets(line_buf, 1024, stdin) != NULL)
  {
    tok = strtok(line_buf, " \n");

    while (tok != NULL && running)
    {
      if (strcmp(tok, "EOF") == 0)
      {
        running = 0;
      }
      else
      {
        int len = strlen(tok);
        int end_cmd = 0;

        if (len > 0 && tok[len - 1] == ';')
        {
          end_cmd = 1;
          tok[len - 1] = '\0';
        }
        if (strcmp(tok, ";") == 0)
        {
          end_cmd = 1;
          tok[0] = '\0';
        }

        if (strlen(tok) > 0)
        {
          if (state == 0)
          {
            if (strcmp(tok, "=") == 0)
              state = 1;
          }
          else if (state == 1)
          {
            strcpy(dest_var, tok);
            state = 2;
          }
          else if (state == 2)
          {
            if (is_num(tok))
            {
              push(&s, atoi(tok));
            }
            else if (strcmp(tok, "+") == 0)
            {
              int b = pop(&s);
              push(&s, pop(&s) + b);
            }
            else if (strcmp(tok, "-") == 0)
            {
              int b = pop(&s);
              push(&s, pop(&s) - b);
            }
            else if (strcmp(tok, "*") == 0)
            {
              int b = pop(&s);
              push(&s, pop(&s) * b);
            }
            else
            {
              push(&s, get_val(&tbl, tok));
            }
          }
        }

        if (end_cmd && state == 2)
        {
          int res = pop(&s);
          set_val(&tbl, dest_var, res);
          stack_clear(&s);
          state = 0;
        }
      }
      tok = strtok(NULL, " \n");
    }
  }

  int i = 0;
  while (i < tbl.total)
  {
    printf("%s = %d\n", tbl.list[i].name, tbl.list[i].val);
    i++;
  }

  stack_free(&s);
  return 0;
}

void stack_init(Stack *s)
{
  s->cap = 10;
  s->data = (int *)malloc(s->cap * sizeof(int));
  if (s->data == NULL)
  {
    printf("Failled to allocate. exiting.\n");
    exit(1);
  }
  s->count = 0;
}

void push(Stack *s, int val)
{
  if (s->count == s->cap)
  {
    s->cap *= 2;
    int *temp = (int *)realloc(s->data, s->cap * sizeof(int));
    if (temp == NULL)
    {
      printf("Failed to reallocate. exiting\n");
      stack_free(s);
      exit(1);
    }
    s->data = temp;
  }
  s->data[s->count] = val;
  s->count++;
}

int pop(Stack *s)
{
  s->count--;
  return s->data[s->count];
}

void stack_clear(Stack *s)
{
  s->count = 0;
}

void stack_free(Stack *s)
{
  free(s->data);
}

int get_val(Table *tbl, char *name)
{
  int val = 0;
  int i = 0;
  int found = 0;
  while (i < tbl->total && !found)
  {
    if (strcmp(tbl->list[i].name, name) == 0)
    {
      val = tbl->list[i].val;
      found = 1;
    }
    i++;
  }
  return val;
}

void set_val(Table *tbl, char *name, int val)
{
  int i = 0;
  int found = 0;
  while (i < tbl->total && !found)
  {
    if (strcmp(tbl->list[i].name, name) == 0)
    {
      tbl->list[i].val = val;
      found = 1;
    }
    i++;
  }
  if (!found)
  {
    strcpy(tbl->list[tbl->total].name, name);
    tbl->list[tbl->total].val = val;
    tbl->total++;
  }
}

int is_num(char *str)
{
  if (strlen(str) == 0)
    return 0;
  int digit = (str[0] >= '0' && str[0] <= '9');
  int neg = (str[0] == '-' && str[1] >= '0' && str[1] <= '9');
  return digit || neg;
}

