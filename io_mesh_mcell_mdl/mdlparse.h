#ifndef MDLPARSE_H
#define MDLPARSE_H

#include <sys/types.h>

typedef unsigned int u_int;

#define YY_DECL int mdllex \
  (YYSTYPE * yylval_param , yyscan_t yyscanner)

struct element_list {
  struct element_list *next;
  u_int begin;
  u_int end;
};


#endif
