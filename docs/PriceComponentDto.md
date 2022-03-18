# PriceComponentDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | The total, calculated price of this component. | 
**label** | **str** | The label associated with this price component. Will be taken from the parent Projects ProjectInformation. | [optional] 
**values** | [**list[CalculationDto]**](CalculationDto.md) | The single Calculation elements this price component is composed of. | [optional] 
**project_catalogues** | [**list[CatalogueDto]**](CatalogueDto.md) | These are Catalogues that are used within this PriceComponent. Catalogues are used to describe catalogues, or collections, that can be used to describe elements with commonly known properties. For example, QuantityAssignments use these to categorize themselves. They are propagate to all child elements, e.g. other containers and QuantityAssignments. In the context of a ServiceSpecification, all elements share the same instance of the collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


