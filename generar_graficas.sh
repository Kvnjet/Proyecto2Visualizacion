#!/bin/bash
# =============================================================
# generar_graficas.sh
# Ejecuta InjaX para generar todas las graficas del Proyecto 2
# Uso: ./generar_graficas.sh
# Requiere que el binario 'injax' este en la misma carpeta
# =============================================================

INJAX="./injax"
DATA="./data"
CHARTS="./charts"

# Verificar que el binario existe
if [ ! -f "$INJAX" ]; then
  echo "ERROR: No se encontro el binario injax en la carpeta actual."
  echo "Colocalo aqui: $(pwd)/injax"
  exit 1
fi

echo "Generando graficas SVG..."

# Univariables
$INJAX $DATA/u1_depresion.json    $CHARTS/u1_depresion.inja    $CHARTS/u1_depresion.svg
echo "  [OK] u1_depresion.svg"

$INJAX $DATA/u2_cgpa.json         $CHARTS/u2_cgpa.inja         $CHARTS/u2_cgpa.svg
echo "  [OK] u2_cgpa.svg"

$INJAX $DATA/u3_genero.json       $CHARTS/u3_genero.inja       $CHARTS/u3_genero.svg
echo "  [OK] u3_genero.svg"

# Bivariables
$INJAX $DATA/bi1_cgpa_dep.json    $CHARTS/bi1_cgpa_dep.inja    $CHARTS/bi1_cgpa_dep.svg
echo "  [OK] bi1_cgpa_dep.svg"

$INJAX $DATA/bi2_ansiedad_anio.json $CHARTS/bi2_ansiedad_anio.inja $CHARTS/bi2_ansiedad_anio.svg
echo "  [OK] bi2_ansiedad_anio.svg"

$INJAX $DATA/bi3_dep_genero.json  $CHARTS/bi3_dep_genero.inja  $CHARTS/bi3_dep_genero.svg
echo "  [OK] bi3_dep_genero.svg"

# Multidimensional
$INJAX $DATA/multi_paralelas.json $CHARTS/multi_paralelas.inja $CHARTS/multi_paralelas.svg
echo "  [OK] multi_paralelas.svg"

# Facetas
$INJAX $DATA/facets_genero.json   $CHARTS/facets_genero.inja   $CHARTS/facets_genero.svg
echo "  [OK] facets_genero.svg"

# Página Web
$INJAX $DATA/index.json           $CHARTS/index.inja           index.html
echo "  [OK] index.html"

echo ""
echo "Listo. SVGs generados en: $CHARTS/"
ls $CHARTS/*.svg
