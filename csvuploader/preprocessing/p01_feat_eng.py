import pandas as pd

def feature_engineering(df_clean):
    df_feat_eng = df_clean.copy()

    # Crear columnas día, mes, año y hora a partir de la fecha
    df_feat_eng['invoice_day'] = df_feat_eng.invoice_date.dt.day
    df_feat_eng['invoice_month'] = df_feat_eng.invoice_date.dt.month
    df_feat_eng['invoice_year'] = df_feat_eng.invoice_date.dt.year
    df_feat_eng['invoice_hour'] = df_feat_eng.invoice_date.dt.hour

    # Eliminar la columna de fecha
    df_feat_eng.drop(columns='invoice_date', inplace=True)

    # Cear columna de ventas totales (quantity * unit_price)
    df_feat_eng['total_sales'] = df_feat_eng['quantity'] * df_feat_eng['unit_price']                                     # Total de ventas por factura
    sales_per_customer = df_feat_eng.groupby('customer_id').agg(sales_per_customer=('total_sales', 'sum')).reset_index() # Agrupar por ventas totales por cliente y renombrar la columna
    df_feat_eng = df_feat_eng.merge(sales_per_customer, on='customer_id', how='left')                                    # Merge sales_customer para cada factura

    # Crear columna con No. de Facturas por cliente
    invoices_per_customer = df_feat_eng.groupby('customer_id').agg(invoices_per_customer=('invoice_no', 'count')).reset_index() # Agrupar las facturas por cliente y renombrar la columna
    df_feat_eng = df_feat_eng.merge(invoices_per_customer, on='customer_id', how='left')                                        # Unir las facturas por cliente con el dataFrame original

    # Crear columna con el valor prom. de factura por cliente
    df_feat_eng['avg_sales_per_customer'] = df_feat_eng['sales_per_customer'] / df_feat_eng['invoices_per_customer']

    # Calcular la cantidad de facturas negativas por usuario 
    neg_invoices_per_customer = df_feat_eng[df_feat_eng['quantity'] < 0].groupby('customer_id').agg(neg_invoices_per_cusotmer=('customer_id', 'count')).reset_index() # Contar las facturas con cantidades negativas
    df_feat_eng = df_feat_eng.merge(neg_invoices_per_customer, on='customer_id', how='left')                                                                          # Asignar los valores a cada factura

    return df_feat_eng.head()