import {
  createContext,
  Dispatch,
  SetStateAction,
  useContext,
  useState,
} from "react";
import { WithChildren } from "../types";
import { serialize } from "../utils";

export type STLInputObjectValues = {
  slotSizeX: number;
  slotSizeY: number;
  slotSizeZ: number;
  numberOfSlotsX: number;
  numberOfSlotsY: number;
  wallThickness: number;
  wallInset: number;
};

export type STLInputObject = STLInputObjectValues & {
  url: string;
  setSlotSizeX: Dispatch<SetStateAction<number>>;
  setSlotSizeY: Dispatch<SetStateAction<number>>;
  setSlotSizeZ: Dispatch<SetStateAction<number>>;
  setNumberOfSlotsX: Dispatch<SetStateAction<number>>;
  setNumberOfSlotsY: Dispatch<SetStateAction<number>>;
  setWallThickness: Dispatch<SetStateAction<number>>;
  setWallInset: Dispatch<SetStateAction<number>>;
  setValues: (values: STLInputObjectValues) => void;
};

const defaultSTLInputContextValue: STLInputObject = {
  // value
  slotSizeX: 30,
  slotSizeY: 30,
  slotSizeZ: 30,
  numberOfSlotsX: 3,
  numberOfSlotsY: 3,
  wallThickness: 1,
  wallInset: 0,
  url: "",
  // functions
  setSlotSizeX: () => {},
  setSlotSizeY: () => {},
  setSlotSizeZ: () => {},
  setNumberOfSlotsX: () => {},
  setNumberOfSlotsY: () => {},
  setWallThickness: () => {},
  setWallInset: () => {},
  setValues: (values: STLInputObjectValues) => {},
};

export const STLInputContext = createContext(defaultSTLInputContextValue);
export const STLInputProvider = STLInputContext.Provider;

export function WithSTLInputContext({ children }: WithChildren) {
  const [slotSizeX, setSlotSizeX] = useState<number>(30);
  const [slotSizeY, setSlotSizeY] = useState<number>(30);
  const [slotSizeZ, setSlotSizeZ] = useState<number>(30);
  const [numberOfSlotsX, setNumberOfSlotsX] = useState<number>(3);
  const [numberOfSlotsY, setNumberOfSlotsY] = useState<number>(3);
  const [wallThickness, setWallThickness] = useState<number>(1);
  const [wallInset, setWallInset] = useState<number>(1);

  const setValues = (values: STLInputObjectValues) => {
    setSlotSizeX(values.slotSizeX);
    setSlotSizeY(values.slotSizeY);
    setSlotSizeZ(values.slotSizeZ);
    setNumberOfSlotsX(values.numberOfSlotsX);
    setNumberOfSlotsY(values.numberOfSlotsY);
    setWallThickness(values.wallThickness);
    setWallInset(values.wallInset);
  };

  const queryString = serialize({
    ssx: slotSizeX,
    ssy: slotSizeY,
    ssz: slotSizeZ,
    nx: numberOfSlotsX,
    ny: numberOfSlotsY,
    wt: wallThickness,
    wi: wallInset,
    v: new Date().valueOf(),
  });

  const url = `/generate-cube-stl?${queryString}`;

  const values = {
    slotSizeX,
    slotSizeY,
    slotSizeZ,
    numberOfSlotsX,
    numberOfSlotsY,
    wallThickness,
    wallInset,
    // TODO with lid cutout
    // TODO with pull tab
    url,
  };

  const functions = {
    setSlotSizeX,
    setSlotSizeY,
    setSlotSizeZ,
    setNumberOfSlotsX,
    setNumberOfSlotsY,
    setWallThickness,
    setWallInset,
    setValues,
  };

  const value = { ...values, ...functions, values, functions };

  return <STLInputProvider value={value}>{children}</STLInputProvider>;
}

export const useSTLInputContext = () => useContext(STLInputContext);
