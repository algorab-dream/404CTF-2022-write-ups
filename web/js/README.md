## Fiché JS

### Description

L'objectif de ce challenge est de réussir à passer le portail de connexion via un code PIN. En fouillant le site, on trouve un fichier ``inedx.js``, donc l'une des fonctions interpelle :
```javascript
Function(
  "HahaAhAhHahahHAaaHhhhHah[...]aaHhhhHhhhHahaAhAhAhAhaAaAaAaAhHAaaaAaA".replace(
    /Haha|AhAh|Haa|AAAH|hHAaa|aAaA|hhaaa|Hhhh/g,
    function (_) {
      return _ == "Haha"
        ? "["
        : _ == "AhAh"
        ? "]"
        : _ == "Haa"
        ? "{"
        : _ == "AAAH"
        ? "}"
        : _ == "hHAaa"
        ? "("
        : _ == "aAaA"
        ? ")"
        : _ == "Hhhh"
        ? "!"
        : _ == "hhaaa"
        ? "+"
        : "";
    }
  )
)();
```
Ce code obfusqué cache certainement le fonction de vérification du code PIN, à nous donc de chercher un moyen de la comprendre.

### Solution

Afin de lire le résultat de la fonction, on peut appeler la méthode ``toString()``, ce qui nous donne :
```javascript
>>  Function(
    "HahaAhAhHahahHAaaHhhhHah[...]aaHhhhHhhhHahaAhAhAhAhaAaAaAaAhHAaaaAaA".replace(
        /Haha|AhAh|Haa|AAAH|hHAaa|aAaA|hhaaa|Hhhh/g,
        function (_) {
        return _ == "Haha"
            ? "["
            : _ == "AhAh"
            ? "]"
            : _ == "Haa"
            ? "{"
            : _ == "AAAH"
            ? "}"
            : _ == "hHAaa"
            ? "("
            : _ == "aAaA"
            ? ")"
            : _ == "Hhhh"
            ? "!"
            : _ == "hhaaa"
            ? "+"
            : "";
        }
    )
    )();
function anonymous(
) {
[][(![]+[])[!+[]+!![]+!![]]+([]+[...]+[]+!![]]))()
}"
```
Cette fonction semble donc renvoyer du [native code javascript](https://www.techtarget.com/searchapparchitecture/definition/native-code). Pour le lire, on peut encore une fois appeler la méthode ``toString``:
```javascript
>>  [][(![]+[])[!+[]+!![]+!![]]+([]+[...]+[]+!![]])).toString()
function anonymous(
) {
/* FONCTIONNEMENT */
var key = $(".keypad").keypad(function (pin) {
  if (pin == "240801300505131273100172") {
    document.location.href = "./nob03y_w1lL_Ev3r_fiNd_th15_PaGe.html";
  }
});
}
```
On a donc le flag en se rendant sur la page indiquée dans le script : 404CTF{Haha_J3_5ui$_f4N_dObfu5c4tIoN_en_JS}.
