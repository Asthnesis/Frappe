// Copyright (c) 2025, Edward Rasto and contributors
// For license information, please see license.txt

frappe.listview_settings['Transaction'] = {
    get_indicator: function(doc) {
        if (doc.lending_status === "Issued") {
            return [__("Issued"), "red", "lending_status,=,Issued"];
        } else if (doc.lending_status === "Returned") {
            return [__("Returned"), "green", "lending_status,=,Returned"];
        } else {
            return [__(doc.lending_status), "grey", "lending_status,=," + doc.lending_status];
        }
    }
};
