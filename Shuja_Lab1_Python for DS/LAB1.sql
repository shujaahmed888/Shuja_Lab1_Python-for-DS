-- Insert into the supplier table
INSERT INTO supplier (SUPP_ID, SUPP_NAME, SUPP_CITY, SUPP_PHONE)
VALUES
    (1, 'Rajesh Retails', 'Delhi', '1234567890'),
    (2, 'Appario Ltd.', 'Mumbai', '258963147032'),
    (3, 'Knome products', 'Bangalore', '9785462315'),
    (4, 'Bansal Retails', 'Kochi', '8975463285'),
    (5, 'Mittal Ltd.', 'Lucknow', '7898456532');

-- Insert into the customer table
INSERT INTO customer (CUS_ID, CUS_NAME, CUS_PHONE, CUS_CITY, CUS_GENDER)
VALUES
    (1, 'AAKASH', '9999999999', 'DELHI', 'M'),
    (2, 'AMAN', '9785463215', 'NOIDA', 'M'),
    (3, 'NEHA', '9999999998', 'MUMBAI', 'F'),
    (4, 'MEGHA', '9994562399', 'KOLKATA', 'F'),
    (5, 'PULKIT', '7895999999', 'LUCKNOW', 'M');

-- Insert into the category table
INSERT INTO category (CAT_ID, CAT_NAME)
VALUES
    (1, 'BOOKS'),
    (2, 'GAMES'),
    (3, 'GROCERIES'),
    (4, 'ELECTRONICS'),
    (5, 'CLOTHES');

-- Insert into the product table
INSERT INTO product (PRO_ID, PRO_NAME, PRO_DESC, CAT_ID)
VALUES
    (1, 'GTA V', 'DFJDJFDJFDJFDJFJF', 2),
    (2, 'TSHIRT', 'DFDFJDFJDKFD', 5),
    (3, 'ROG LAPTOP', 'DFNTTNTNTERND', 4),
    (4, 'OATS', 'REURENTBTOTH', 3),
    (5, 'HARRY POTTER', 'NBEMCTHTJTH', 1);

-- Insert into the orders table
INSERT INTO order_table (ORD_ID, ORD_AMOUNT, ORD_DATE, CUS_ID, PROD_ID)
VALUES
    (20, 1500, '2021-10-12', 3, 5),
    (25, 30500, '2021-09-16', 5, 2),
    (26, 2000, '2021-10-05', 1, 1),
    (30, 3500, '2021-08-16', 4, 3),
    (50, 2000, '2021-10-06', 2, 1);

-- Insert into the rating table
INSERT INTO rating (RAT_ID, CUS_ID, SUPP_ID, RAT_RATSTARS)
VALUES
    (1, 2, 2, 4),
    (2, 3, 4, 3),
    (3, 5, 1, 5),
    (4, 1, 3, 2),
    (5, 4, 5, 4);
