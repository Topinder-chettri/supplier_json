from django.shortcuts import render
import json
# Create your views here.
def sup(request):
    json_data = {
 "crate_table": [
  {
   "crate": "3e410b75b4",
   "crate_weight": 18100,
   "creation": "2022-08-24 16:22:13.985299",
   "docstatus": 0,
   "doctype": "Crate Procurement Table",
   "idx": 1,
   "is_final_crate": "0",
   "modified": "2022-08-24 16:22:14.271881",
   "modified_by": "grn@iotready.co",
   "name": "0654b30ec0",
   "owner": "grn@iotready.co",
   "packed_quantity": 18100,
   "parent": "SOMEID-SOMEHUB-24082022",
   "parentfield": "crate_table",
   "parenttype": "Procurement Summary",
   "sku": "10000298"
  },
  {
   "crate": "7c2eba029c",
   "crate_weight": 18090,
   "creation": "2022-08-24 16:22:13.985299",
   "docstatus": 0,
   "doctype": "Crate Procurement Table",
   "idx": 2,
   "is_final_crate": "0",
   "modified": "2022-08-24 16:22:14.271881",
   "modified_by": "grn@iotready.co",
   "name": "1b888f5741",
   "owner": "grn@iotready.co",
   "packed_quantity": 18090,
   "parent": "SOMEID-SOMEHUB-24082022",
   "parentfield": "crate_table",
   "parenttype": "Procurement Summary",
   "sku": "10000298"
  }
 ],
 "creation": "2022-08-24 16:22:13.985299",
 "docstatus": 0,
 "doctype": "Procurement Summary",
 "grn": 'null',
 "hub": "SOMEHUB",
 "idx": 0,
 "modified": "2022-08-24 16:22:14.271881",
 "modified_by": "grn@iotready.co",
 "name": "SOMEID-SOMEHUB-24082022",
 "owner": "grn@iotready.co",
 "parent": 'null',
 "parentfield": 'null',
 "parenttype": 'null',
 "sku_table": [
  {
   "creation": "2022-08-24 16:22:14.280143",
   "docstatus": 0,
   "doctype": "SKU Procurement Table",
   "idx": 1,
   "modified": "2022-08-24 16:22:14.280143",
   "modified_by": "grn@iotready.co",
   "name": "7b71370782",
   "owner": 'null',
   "parent": "SOMEID-SOMEHUB-24082022",
   "parentfield": "sku_table",
   "parenttype": "Procurement Summary",
   "quantity": 36190,
   "sku": "10000298",
   "sku_description": "Mango Banganapalli 1 kg",
   "standard_crate_quantity": 18000
  }
 ],
 "supplier": "SOMEID",
 "supplier_name": "Sunil N"
}
    return render(request, 'temp/suppliers.html', {"json_data": json_data})
    
