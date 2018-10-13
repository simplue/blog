if [ -z $1 ]; then
  echo 'error: no argument supplied'
  exit 1
fi

if [ -d $1 ]; then
  echo 'error: dir exists'
  exit 1
fi

mkdir $1
cd $1
mkdir css js

echo '<!DOCTYPE>' > index.html
echo '<title>Hello</title>' >> index.html
echo '<h1>Hi</h1>' >> index.html

echo 'h1{color: red;}' > css/style.css

echo 'var string = "Hello World"' > js/main.js
echo 'alert(string)' >> js/main.js

echo 'success'
exit 0
