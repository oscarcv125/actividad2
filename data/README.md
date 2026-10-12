# Corpus sintético de soporte

Son ejemplos inventados para el curso, no hay personas reales ni datos comerciales.

Columnas: id (fila), family (variantes de una misma solicitud), split (train/validation/test), label (categoría), text_original y text_processed (con NFC y espacios limpios). Categorías: acceso, pagos, conectividad y software. Si un mensaje mezcla un problema resuelto con uno vigente, se etiqueta el vigente.

El modelo solo usa text_processed, nunca id/family/split/label como features. Las particiones ya están fijas desde antes de entrenar.

Es un corpus chico y parejo a propósito, para enfocarse en representación y evaluación, no en generalizar a casos reales. Para esta Actividad 2 son 40 familias (6 train, 2 validation, 2 test por categoría) y no toca los datos de entregas anteriores.

Si vas a reusar tu corpus de la A1, respeta sus particiones y que tenga al menos 2 categorías en train. No lo fuerces a parecerse a este.

En el ZIP, apoyos/ trae las presentaciones y notebooks de Clases 3-4 con sus datos en apoyos/data/.
