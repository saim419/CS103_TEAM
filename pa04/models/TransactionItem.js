
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var transactionSchema = Schema( {
  item: String,
  completed: Boolean,
  createdAt: Date,
  Category: String,
  Amount: Number,
  Date: String,
  Description: String,
  //priority: Number,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'TransactionItem', transactionSchema );
