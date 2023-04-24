# LanguageSyntaxGuide

**1. LetParsing**

```
Syntax: let (variable assign) in (body) end
Example:leta= 1 inprinta> 0 end
```
**2. If-Elsestatement**

```
Syntax: if (condition) then (body) else (body) end
Example:iftruethen 3 + 4 else 5
```
**3. Forloop**

```
Syntax: for (condition) up (update statement) do (body) end
```
```
Example:leta= 1 infora< 10 upa++doprintaend
```
**4. SimpleStatementsandOperators**

```
Syntax(Example) :i) 3 > 4 end
ii)leta= 1 inletb= 1 inprintb<=aend
iii)leta= 2 inletb= 9 inprintb+=aend
```
**5. ListParsingandMethodCalling**

```
Keyword: Explicit“list”keywordhasbeendefined.
Syntax: let (variable)= list[ (values) ] in (body) end
Example: i)leta=list[ 1 , 2 , 3 , 4 , 5 ]inprintaend
```

```
MethodCalling:
Method classhas been defined for this purpose.It has a method name and
identifier.
Syntax: (variable).method_name
Example: i)leta=list[ 1 , 2 , 3 , 4 , 5 ]inprinta.lengthend
```
```
ListMethods:
```
```
1 ) Get Methodforfetchingelementfromspecificindex:
Example: letl=list[ 1 , 2 , 4 ]inletb=l.get 1 inprintbend
```
```
2 ) Assign Methodforassigningelementtospecificindex:
Example :letl=list[ 1 , 2 , 3 ]inletb=l.assign 234 inprintlend
```
```
3 ) Append Methodforappendingatlastofthelist:
Example: letl=list[ 1 , 2 , 3 ]in{
l.append 4 ;
printl;
}
```
**6. StringParsingandMethodCalling**

```
Keyword: Explicit“String”keywordhasbeendefined.
Syntax: let (variable)= String “ string ” in (body) end
Example:
i)leta=String“helloworld”inprintaend
ii)leta=String“helloworld”inprinta.lengthend
StringMethods:
```
```
1 ) Concat Method:ConcatMethodconcatenatestwostrings.
Example:
lets=String"hello"in
letb=String"World!"in
letans=s.concatbin
printans
end
```
```
2 ) Slice Method:Slicemethodslicesthestring.
```

```
Example:
lets=String"hello"in
letb=s.slice 031 in
printbend
```
```
Here 0 :start 3 :stop 1 :step
```
**7. BitwiseOperators**
    **Syntax(Example):** i) 6 & 3 end
       ii) 5 | 2 end
       iii) 2 ^ 7 end
       iv) 8 << 2 end
       v) 4 >> 1 end

```
(Note:Thebitwiseoperatorsareyettobeimplementedonvariables.)
```
**8. UnaryOperators**
    **Syntax:** (variable) **++** , (variable) **--** , **-** (variable)
    **Example:**
    i) leta= 1 infora< 2 upa++doprinta+ 2 inletb= 1 inprintbend
    ii)leta= 10 inletb= 1 infora> 0 upa--doprinta+bend

**9. SequenceParsing**
Sequenceinourlanguagebeginswith“{“Markerandendswith“}”Marker.For
innersequences“;”isadded.

```
Example
i)leta= 1 in
letb= 20 in
{
printa;
printb;
printa+b;
}
ii)
```

```
letfunf(a,b,c)=a*b*cin
letfunsum(a,b)=a+bin
{
printf( 1 , 4 , 3 );
printsum(f( 1 , 3 , 4 ),f( 2 , 10 , 2 ));
}
end
```
**10 .FunctionParsing
Syntax: letfun** (variable) (params) = function body **in**
(rest_code body)

```
Example:
i)letfunfact(n)=ifn== 0 then 1 elsen*fact(n- 1 )inprintfact( 3 )end
ii)
letfunf(a,b,c)=a*b*cin
letfunsum(a,b)=a+bin
{
printf( 1 , 4 , 3 );
printsum(f( 1 , 3 , 4 ),f( 2 , 10 , 2 ));
}
end
```

